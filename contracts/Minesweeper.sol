// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Minesweeper is ERC721, Ownable {
    uint256 public tokenCounter;
    mapping(uint256 => address) public winners;

    constructor() ERC721("MinesweeperNFT", "MSW") {
        tokenCounter = 0;
    }

    function createNFT(address player) public onlyOwner returns (uint256) {
        uint256 newTokenId = tokenCounter;
        _safeMint(player, newTokenId);
        winners[newTokenId] = player;
        tokenCounter += 1;
        return newTokenId;
    }

    // Additional game-related functions can be added here
}
