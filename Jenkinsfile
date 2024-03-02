pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'radhika20/scientific-calculator'
        DOCKER_HUB_CREDENTIALS = 'docker-hub-credentials'
        ANSIBLE_CONFIG = '/home/radhika/ansible-projects/ansible.cfg'
        PYTHON_INTERPRETER = '/usr/bin/python3'
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
                        sh 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin'
                    }
                }
            }
        }
        stage('Preparation') {
    steps {
        script {
            sh ' pip3 install docker'// Attempts to install with pip first, then pip3
        }
    }
}


       stage('Deploy with Ansible') {
            steps {
                script {
                    
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory',
                        become: true, // Ensure Ansible uses sudo
                       extras: "-vvv --extra-vars ansible_become_pass=radhika1 --extra-vars ansible_python_interpreter=${PYTHON_INTERPRETER}"  // Verbose mode for debugging
                    )
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
