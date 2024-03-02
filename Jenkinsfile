pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'radhika20/scientific-calculator'
        DOCKER_HUB_CREDENTIALS = 'docker-hub-credentials'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Docker Push') {
            steps {
                script {
            withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
            }
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                script {
        
           withCredentials([usernamePassword(credentialsId: 'YourCredentialID', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                     sh '/usr/bin/ansible-playbook -i inventory deploy.yml  -e docker_user=$DOCKER_USER -e docker_pass=$DOCKER_PASS'
                } 
                }
        
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}
