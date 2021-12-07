import React from "react";
import styled from "styled-components";

export default function Hand(props) {
  const hand = props.hand;
  return (
    <HandContainer>
      <p>
        Hole cards: {hand.holeCardOne} {hand.holeCardTwo}
      </p>
      <p>
        Flop: {hand.flopCardOne}
        {hand.flopCardTwo}
        {hand.flopCardThree}
      </p>
      <p>Turn: {hand.turnCard}</p>
      <p>River: {hand.riverCard}</p>
    </HandContainer>
  );
}

const HandContainer = styled.div`
  border-radius: 5px;
  background-color: #121212;
  padding: 10px;
  color: white;
  margin-top: 5px;
  margin-bottom: 5px;
`;
