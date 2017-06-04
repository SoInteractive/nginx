#!groovy

/* Only keep the 10 most recent builds. */
/*def projectProperties = [
    [$class: 'BuildDiscarderProperty',strategy: [$class: 'LogRotator', numToKeepStr: '5']],
]

properties(projectProperties)*/

/* Declarative pipeline */
pipeline {
  agent {
    node {
      label 'master'
      customWorkspace 'workspace/nginx'
    }
  }
  stages {
    stage('Prepare environment') {
      steps {
        sh 'molecule create'
        sh 'molecule converge'
      }
    }
    stage('Check syntax') {
      steps {
        sh 'molecule syntax'
      }
    }
    stage('Run Tests'){
      steps {
        sh 'molecule idempotence'
        sh 'molecule verify'
      }
    }
  }

  post {
    always {
      sh 'molecule destroy'
    }
    success {
      mattermostSend color: 'good', message: "Job ${JOB_NAME} ${BUILD_NUMBER} has finished successfully (<${BUILD_URL}|Open>)"
    }
    failure {
      mattermostSend color: 'danger', message: "Job ${JOB_NAME} ${BUILD_NUMBER} has failed(<${BUILD_URL}|Open>)"
    }
  }
}
