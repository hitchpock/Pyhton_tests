
pipeline{
    agent any
    stages{
        stage("Build"){
            steps{
                // echo "========executing Build========"
                sh """python3 -m venv venv
                 . venv/bin/activate
                 pip install -r requirements.txt
                 pip install -e . """
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========Build executed successfully========"
                }
                failure{
                    echo "========Build execution failed========"
                }
            }
        }
        stage("Test"){
            steps{
                echo "========executing Test========"
                sh """ . venv/bin/activate
                cd Test/
                pytest --setup-show test_hello.py -s -q"""
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========Test executed successfully========"
                }
                failure{
                    echo "========Test execution failed========"
                }
            }
        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}