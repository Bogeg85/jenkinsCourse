#!/usr/bin/env groovy
pipeline {
    agent any

    stages {
        stage("checkout") {
            steps {
                echo "*************checkout************"
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Bogeg85/jenkinsCourse.git']]])
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
