pipeline {
    agent none 
    stages {
        stage ('Deploy') {
            agent {
                node {
                    label 'deploy'
                }
            }
            steps {
                sshagent(credentials: ['cloudlab']) {
                    sh 'scp -r -v -o StrictHostKeyChecking=no *.yaml MH824134@clnodevm157-1.clemson.cloudlab.us:~/'
                    sh 'ssh -o StrictHostKeyChecking=no MH824134@clnodevm157-1.clemson.cloudlab.us kubectl apply -f /users/MH824134/redis.yaml -n jenkins'
                    sh 'ssh -o StrictHostKeyChecking=no MH824134@clnodevm157-1.clemson.cloudlab.us kubectl apply -f /users/MH824134/redis-service.yaml -n jenkins'                                        
                }
            }
        }
    }
}
