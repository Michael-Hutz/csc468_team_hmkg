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
                    sh 'scp -r -v -o StrictHostKeyChecking=no *.yaml mh824134@clnodevm063-1.clemson.cloudlab.us:~/'
                    sh 'ssh -o StrictHostKeyChecking=no mh824134@clnodevm063-1.clemson.cloudlab.us kubectl apply -f /users/mh824134/redis.yaml -n jenkins'
                    sh 'ssh -o StrictHostKeyChecking=no mh824134@clnodevm063-1.clemson.cloudlab.us kubectl apply -f /users/mh824134/redis-service.yaml -n jenkins'                                        
                }
            }
        }
    }
}
