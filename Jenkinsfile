pipeline {

agent any

stages{

stage('Clone') {
 steps {
          git branch: 'main', url:'https://github.com/marwanfursa3/kaltura.git'
       
    }  
}
stage('Build') {
   steps {
    
 //   sh './mvnw package'
     sh	 'pip3 install -r requirments.txt'
   
    }  
}

stage('run') {
   steps {
    sh 'python3 main.py'    

    }  
}
stage('run') {
   steps {
 
    sh slackSend channel: "jenkins", message: "Hey From Slack -- IT WORKS "
   }
}
}

}
