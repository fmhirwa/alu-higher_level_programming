#!/usr/bin/node

const Rectangle = require('../javascript_objects_scopes_closures/4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
