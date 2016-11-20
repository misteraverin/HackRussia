pragma solidity ^0.4.2;

contract BuySell {
    mapping (address => uint) quantity;
    

    event Send(address from, address to, uint value);
    struct Offer{
        address sender;
        uint price;
        bytes type;
        uint quantity;
    }
    
    uint numOfferings = 0;
    mapping (uint => Offer) offerings;
    
    function newOffer(address sender, uint price, bytes type, uint quantity) returns (uint offerID) {
       offerID = numOfferings++;
       offerings[offerID] = Offer(sender, price, type, quantity);
    }
    
    function TenderProperty(address type, uint amount, uint quantity, uint price) {
        // amount is the number of things BUYER wishes to buy
        // quantity is the number of things SOMEBODY actually has
        if (amount < quantity[type]) return;
        offerings = newOffer(msg.sender, price, type, quantity);
        
    } 
    function BuyProperty(address offerer, address type, uint offerID, uint amount, uint quantity) {
        if (msg.value < msg.sender[type][1] * amount) return;
        if (offerings[offerID][3] < amount) return;
        offerings[offerID][3] -= amount;
        quantity[msg.sender] += amount;
        Send(msg.sender, offerer, msg.sender[type][1] * amount);
    }
    function queryQuantity(address addr) constant returns (uint msg.sender[type][2]) {    }
}
