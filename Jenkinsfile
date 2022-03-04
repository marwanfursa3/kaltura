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
    sh """
   	
    pip3 install -r requirements.txt
    """
    }  
}

//stage('run') {
  // steps {
 //   sh 'python3 main.py'    
//
  //  }  
//}

}

}
