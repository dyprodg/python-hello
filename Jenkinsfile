pipeline {
    agent { label 'python-tester' }

    stages {
        stage('Set up Python environment') {
            steps {
                script {
                    // Einrichten einer virtuellen Umgebung
                    sh 'python -m venv venv'
                    sh '. ./venv/bin/activate'

                    // Installieren von Abhängigkeiten aus requirements.txt
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    // Aktivieren der virtuellen Umgebung und Ausführen von Tests
                    sh '. ./venv/bin/activate'
                    sh 'pytest test_main.py'
                }
            }
        }

        stage('Run main application') {
            steps {
                script {
                    // Aktivieren der virtuellen Umgebung und Ausführen der Hauptanwendung
                    sh '. ./venv/bin/activate'
                    sh 'python main.py'
                }
            }
        }
    }

    post {
        always {
            // Bereinigen nach dem Ausführen der Pipeline
            cleanWs()
        }
    }
}