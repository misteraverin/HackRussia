pragma solidity ^0.4.2;

contract Freelancer {
    
    

    event Send(address from, address to, uint value);
    struct Offer{
        address sender;
        uint price;
        bytes type;
        uint reputation;
        bool availability;
        uint reputation_threshold;
        uint freelancerID;   // what freelancer has taken the job, if applicable
    }
    
    struct Freelancer{
        address sender;
        uint price;
        bytes type;
        uint reputation;
        bool availability;
        uint reputation_threshold;
    }
    
    /* Availability of an offer is true when the job is not "in process" or "done",
    and is false otherwise.
    When the offer is "done", its availability stays false forever.
    When the offer is "in process", its availability can become true if the freelancer
    fails to meet the expectations of employer.
    */
    
    /* Availability of a freelancer is set by freelancer's will. He and only he 
    (or she and only she) decides whether to take the projects or not.
    */
    
    uint jobID = 0;
    uint freelancerID = 0;
    prev_block_timestamp = block.timestamp;
    mapping (uint => Offer) jobs;
    mapping (uint => Freelancer) freelancers;

    function AddJobAsEmployer(uint price, bytes type, uint threshold) {

        jobID++;
        jobs[jobID] = Offer(msg.sender, price, type, 0, true, threshold);
        Send(msg.sender,this.address,jobs[jobID][1]);

    } 
    
    function AddMeAsFreelancer(uint price, bytes type, uint threshold) {

        freelancerID++;
        freelancers[freelancerID] = Freelancer(msg.sender, price, type, 0, true, threshold);

    } 
    
    function ChangeAvailability(uint freelancerID) returns (bool not_availability) {

        if (freelancers[freelancerID][4] == true) return false;
        if (freelancers[freelancerID][4] == false) return true;
    }
    
    
    function AcceptOffer(uint jobID, uint freelancerID) {
  
  
    if (freelancers[freelancerID][3] >= jobs[jobID][5])
    { 
    // if freelancer's reputation is >= than set by an employer "threshold"
    jobs[jobID][4] = false;  jobs[jobID][6] = freelancerID;
    }
    // the availability of this job becomes false, 
    // the freelancer is set as the performer 
    } 
    
    function ChooseFreelancer(uint jobID, uint freelancerID) {

    if (jobs[jobID][3] >= freelancers[freelancerID][5])
        // if employer's reputation is >= than set by an freelancer "threshold"
    { jobs[jobID][4] = false;  jobs[jobID][6] = freelancerID; 
    // the availability of this job becomes false, 
    // the freelancer is set as the performer 
        Send(msg.sender,this.address,jobs[jobID][1]);
        // employer here sends the payment to this contract
                                                }

    } 
    
  
    /* 
    It's bad if a freelancer takes the job and then suddenly "disappears" when doing it. 
    Thus the penalty and the reward system should take place.
    
    Penalties are given if the freelancer doesn't respond for more than 1 day. 
    If the silence time exceeds 2 days, further reputation points deduction is applied.
    If the silence time exceeds 3 days, the freelancer is automatically released from 
    his duties, and the 'availability' ticker for this job becomes 'true'. 
    
    */
    
    /*
    Honestly, disappearing of employer is also bad for doing the job.
    (we should somehow implement it into our code)
    */
    
    function EmployerInquiry(uint jobID, uint freelancerID) {
           employerTimeInquiry = block.timestamp;
           
      //     FreelancerResponse(jobID, freelancerID, employerTimeInquiry);
            
            
        }
     
     
     function FreelancerResponse(uint jobID, uint freelancerID, uint employerTimeInquiry) {
         
         if (block.timestamp - employerTimeInquiry > 3*60*60*24) //more than 3 days
          EmployerTerminate(jobID, freelancerID);
          
         if (block.timestamp - employerTimeInquiry > 2*60*60*24) //more than 2 days
         {freelancers[freelancerID][3] -= 5; //freelancer loses 5 reputation points
         }
         
         if (block.timestamp - employerTimeInquiry > 60*60*24) //more than 1 day
         {freelancers[freelancerID][3] -= 2; //freelancer loses 2 reputation points
         }
         
         
     }

            
       function EmployerTerminate(uint jobID, uint freelancerID) {
           
           freelancers[freelancerID][3] -= 10; //freelancer loses 10 reputation points
           jobs[jobID][4] = true; //job becomes available for other freelancers 
       }
        
        
        function FreelancerTerminate(uint jobID, uint freelancerID) {
            
            freelancers[freelancerID][3] -= 10; //freelancer loses 10 reputation points
            jobs[jobID][4] = true; //job becomes available for other freelancers 
        } 
        
        function HappyEnd(uint jobID, uint freelancerID) {
            
            Send(this.address,freelancers[freelancerID][0],jobs[jobID][1]);
            
        }
        
        
    }
    
