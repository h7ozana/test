node {
    def app

    stage('Clone repository') {
      

        checkout scm
    }

    stage('Build image') {
  
       app = docker.build("stayc/test")
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
   def DOCKERTAG = "${env.BUILD_NUMBER}"

      stage('Trigger ManifestUpdate') {
          build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: DOCKERTAG)]
  }
}
