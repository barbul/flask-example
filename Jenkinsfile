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
            mail(subject: 'test', body: 'testing', from: 'jenkins', to: 'bartek.bulzak@radio-canada.ca')
          }
        }
        stage('stage2b') {
          steps {
            echo 'stage2b'
          }
        }
      }
    }
  }
}