export default class Building {
  constructor(sqft) {
    if (new.target === Building) {
      throw new Error("Cannot instantiate an abstract class");
    }
    if (typeof sqft !== 'number') {
      throw new Error('sqft must be a number');
    }

    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    throw new Error("Class extending Building must override evacuationWarningMessage");
  }
}
