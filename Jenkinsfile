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
                sh 'DOCKER_BUILDKIT=1 docker build -t $IMAGE .'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    mkdir -p allure-results reports
                    docker run --rm \
                        -u "$(id -u):$(id -g)" \
                        -v "$WORKSPACE/allure-results:/app/allure-results" \
                        -v "$WORKSPACE/reports:/app/reports" \
                        $IMAGE \
                        $TEST_PATH \
                        ${MARKER:+-m "$MARKER"} \
                        -n $WORKERS \
                        -p no:cacheprovider \
                        --alluredir=allure-results \
                        --junitxml=reports/report.xml
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/report.xml'
            allure includeProperties: false, results: [[path: 'allure-results']]
            sh 'docker rmi $IMAGE || true'
            cleanWs()
        }
    }
}