pipeline {

agent any

stages{

stage('Clone') {
 steps {
          git branch: 'main', url:'https://github.com/marwanfursa3/kaltura.git'
       
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
stage('slack') {
   steps {
 
    slackSend color: 'good', message: 'Message from Jenkins Pipeline'
   }
}
stage('slacks') {
   steps {
 
sh' echo heloo > hello.txt'    }
}
}
}

