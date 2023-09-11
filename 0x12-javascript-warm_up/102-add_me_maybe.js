#!/usr/bin/node
exports.addMeMaybe = (number, theFunction) => {
  theFunction(++number);
};
