pipeline {
    agent {
        docker {
            image 'qnib/pytest'
        }
    }

    stages {
        stage("Prerequisites") {
            steps { 
                echo "*******installing pytest************"
                sh 'pip install pytest'
            }
        }
        stage("Run tests") {
            steps {
                echo "*******testing************"
                sh 'pytest'
            }
        }
    }
}
