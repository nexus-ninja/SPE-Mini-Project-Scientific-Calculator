pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'radhika20/scientific-calculator'
        DOCKER_HUB_CREDENTIALS = 'docker-hub-credentials'
        ANSIBLE_CONFIG = '/home/radhika/ansible-projects/ansible.cfg'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Running Docker build command within WSL
                    sh 'wsl docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Docker Push') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKER_HUB_CREDENTIALS, passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        // Logging in to Docker Hub within WSL
                        sh 'wsl echo "$DOCKER_PASSWORD" | wsl docker login -u "$DOCKER_USERNAME" --password-stdin'
                    }
                }
            }
        }

        stage('Preparation') {
            steps {
                script {
                    // Ensuring Docker SDK for Python is installed within WSL's Python environment
                    sh 'wsl -e pip3 install docker'
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                script {
                    // Executing Ansible playbook within WSL, ensuring correct Python interpreter and Docker SDK usage
                    sh '''
                    wsl ansible-playbook -i inventory deploy.yml --become -vvv \
                    --extra-vars "ansible_become_pass=radhika1 ansible_python_interpreter=/usr/bin/python3"
                    '''
                }
            }
        }
    }

    post {
        always {
            // Logging out from Docker within WSL
            sh 'wsl docker logout'
        }
    }
}
