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
                    sh 'echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin'
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                script {
                    sh 'ansible-playbook -i ansible/hosts ansible/deploy_app.yml'
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
