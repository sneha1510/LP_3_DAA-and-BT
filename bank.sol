// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    address public accholder;
    uint256 public balance = 0;

    constructor() 
    {
        accholder = msg.sender; // Whoever deploys the contract becomes the account holder
    }

    // Function to withdraw a specific amount
    //msg is a special global variable that contains information about the current transaction
    function withdraw(uint256 amount) public payable  
    {
        require(amount <= balance, "You cannot withdraw more than your balance.");
        require(msg.sender == accholder, "You are not the account owner.");
    
        //payable keyword allows sending Ether to the address.
        payable(msg.sender).transfer(amount);
        balance -= amount;
    }

    // Function to deposit money into the contract
    function deposit() public payable 
    {
        require(msg.value > 0, "Cannot deposit zero.");
        require(msg.sender == accholder, "You are not the account owner.");

        balance += msg.value; // Add the deposited amount to balance
    }

    // Function to show the current balance
    function showbal() public view returns (uint256) 
    {
        require(msg.sender == accholder, "You are not the account owner.");
        return balance; // Return the current balance
    }
}
