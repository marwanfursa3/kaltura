pipeline {

agent any

stages{

stage('Clone') {
 steps {
          git branch: 'main', url:'https://github.com/marwanfursa3/kaltura.git'
       
    } 
  post {
                //in case of success : send a success message to my channel in slack
                success {
                            slackSend channel: 'jenkins', message: 'Hey From Slack -- IT WORKS '
                //in case of failure : send a failure message to my channel in slack
                failure {
                        slackSend channel: '#fursa', color: '#FF0000', message: 'Failed build', tokenCredentialId: 'slacks'}
  }
}
// stage('pull') {
                      
//			steps {
				
//				sh 'docker pull marwan1408/news'
//			}
//	}
 // stage('run') {
   //                   
	//		steps {
				
	//			sh 'docker run -it -d -p 5500:5500 marwan1408/news'
	//		}
	//}
//stage('Build') {
  // steps {
    
    // sh	 'pip3 install -r requirments.txt'
   
    //}  
//}

//stage('run') {
  // steps {
  //  sh "JENKINS_NODE_COOKIE=do_not_kill nohup python3 main.py &"    

    //sh "python3 main.py "    

   // }  
//}

}
}

