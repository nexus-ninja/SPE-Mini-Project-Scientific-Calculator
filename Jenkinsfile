pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'radhika20/scientific-calculator'
        GITHUB_REPO_URL = 'https://github.com/radhu20/scientific-calculator.git'
    }

    stages {
        
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code from the GitHub repository
                    git branch: 'main', url: "${GITHUB_REPO_URL}"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE_NAME}", '.')
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script{
                    docker.withRegistry('', 'docker_hub_credentials') {
                    sh 'docker tag scientific-calculator radhika20/scientific-calculator:latest'
                    sh 'docker push radhika20/scientific-calculator'
                    }
                 }
            }
        }

   stage('Run Ansible Playbook') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory'
                     )
                }
            }
        }

    }
}
