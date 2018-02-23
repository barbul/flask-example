pipeline {
  agent any
  stages {
    stage('lint') {
      steps {
        sh '''echo "linting..."
sleep 10
echo "DONE linting"'''
        sleep 2
        echo 'Thanks for waiting'
      }
    }
    stage('stage2') {
      parallel {
        stage('stage2') {
          steps {
            echo 'stage 2'
          }
        }
        stage('stage2b') {
          steps {
            echo 'stage2b'
          }
        }
      }
    }
    stage('stage3') {
      steps {
        echo 'stage 3'
      }
    }
  }
}