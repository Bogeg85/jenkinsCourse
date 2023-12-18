pipeline {
    agent {
        docker {
            image 'qnib/pytest'
        }
    }

    stages {
        stage("Run tests") {
            steps {
                echo "*******testing************"
                sh 'pytest'
            }
        }
    }
}
