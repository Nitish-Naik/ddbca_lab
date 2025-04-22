// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VotingSystem {
    address public owner;

    struct Candidate {
        string name;
        uint voteCount;
    }

    struct Voter {
        bool authorized;
        bool voted;
        uint vote;
    }

    mapping(address => Voter) public voters;
    Candidate[] public candidates;
    uint public totalVotes;

    constructor(string[] memory candidateNames) {
        owner = msg.sender;
        for (uint i = 0; i < candidateNames.length; i++) {
            candidates.push(Candidate(candidateNames[i], 0));
        }
    }

    function authorize(address _person) public {
        require(msg.sender == owner, "Only owner can authorize voters");
        require(!voters[_person].authorized, "Voter is already authorized");
        voters[_person].authorized = true;
    }

    function vote(uint _candidateIndex) public {
        Voter storage sender = voters[msg.sender];
        require(sender.authorized, "You are not authorized to vote");
        require(!sender.voted, "You have already voted");
        require(_candidateIndex < candidates.length, "Invalid candidate");

        sender.vote = _candidateIndex;
        sender.voted = true;
        candidates[_candidateIndex].voteCount++;
        totalVotes++;
    }

    function getCandidateCount() public view returns (uint) {
        return candidates.length;
    }

    function getVotes(uint _candidateIndex) public view returns (uint) {
        require(_candidateIndex < candidates.length, "Invalid candidate index");
        return candidates[_candidateIndex].voteCount;
    }
}



// ["Alice", "Bob", "Charlie"]
