 pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo "Checkout"
                git 'https://github.com/NevenMoore/scf_devops.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building'
                sh "pip install -r requirements.txt"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
                script {
                    ret = sh(script: "scf native invoke -t ./template.yaml --no-event", returnStatus: true)
                    if (ret != 0) {
                        echo '[Test] Failed'
                        currentBuild.result = 'FAILURE'
                        return
                    }                 
                }

            }
        }
        stage('Deploy - Staging') {
            steps {
                echo 'Deploy - Staging'
            }
        }
        stage('Sanity check') {
            steps {
                input "Does the staging environment look ok?"
            }
        }
        stage('Deploy - Production') {
            steps {
                echo 'Deploy - Production'
                script {
                    ret = sh(script: "scf package -t ./template.yaml", returnStatus: true)
                    if (ret != 0) {
                        echo '[Deploy] Failed'
                        currentBuild.result = 'FAILURE'
                        return   
                    }
                    ret = sh(script: "scf deploy -t ./deploy.yaml -f", returnStatus: true)
                    if (ret != 0) {
                        echo '[Deploy] Failed'
                        currentBuild.result = 'FAILURE'
                        return   
                    } 
                }
            }
        }
    }

    post {
        success {
            echo 'I succeeeded!'
        }
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            echo 'I failed :('
        }
        changed {
            echo 'Things were different before...'
        }
    }
}
