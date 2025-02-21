
// SPDX-License-Identifier: MIT
pragma solidity  ^0.8.19;

contract Counter {
    int public counter;

    constructor() {
        counter = 0;
    }
    function increment() public {
        counter += 1;
    }

    function decrement() public {
        counter -= 1;
    }

    function getCounter() public  view  returns (int) {
        return  counter;
    }
}
