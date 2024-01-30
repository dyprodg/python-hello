pipeline {
    agent { label 'ec2-basic' }

    stages {
        stage('Set up Python environment') {
            steps {
                script {
                    // Einrichten einer virtuellen Umgebung
                    sh 'python3 -m venv venv'
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
                    sh 'python3 main.py'
                }
            }
        }
    }
}