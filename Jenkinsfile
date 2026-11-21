pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 60, unit: 'MINUTES')
    }

    parameters {
        string(name: 'TEST_PATH', defaultValue: 'tests', description: 'Путь или выражение для pytest')
        string(name: 'MARKER',    defaultValue: '',      description: 'pytest -m (например smoke)')
        string(name: 'WORKERS',   defaultValue: 'auto',  description: 'Число воркеров xdist')
    }

    environment {
        IMAGE = "autotests:${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Test') {
    steps {
        sh '''
            CONTAINER=autotests-$BUILD_NUMBER
            rc=0
            docker run --name $CONTAINER $IMAGE \
                tests -n 4 -p no:cacheprovider \
                --alluredir=allure-results \
                --junitxml=reports/report.xml || rc=$?

            rm -rf allure-results reports
            docker cp $CONTAINER:/app/allure-results ./allure-results || true
            docker cp $CONTAINER:/app/reports ./reports || true
            docker rm -f $CONTAINER
            exit $rc
        '''
    }
}
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/report.xml'
            allure includeProperties: false, results: [[path: '/app/allure-results']]
            sh 'docker rmi $IMAGE || true'
            cleanWs()
        }
    }
}