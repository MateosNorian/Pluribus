const createCardObj = function (handData) {
  let obj = {
    id: handData[0],
    holeCardOne: handData[1],
    holeCardTwo: handData[2],
    flopCardOne: handData[3],
    flopCardTwo: handData[4],
    flopCardThree: handData[5],
    turnCard: handData[6],
    riverCard: handData[7],
  };

  return obj;
};

export default createCardObj;
