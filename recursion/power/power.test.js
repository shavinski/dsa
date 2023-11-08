import assert from 'assert';
import { power } from './power.js';

describe('Power test', () => {
    it('return proper power of positive number', () => {
        assert.equal(power(2, 2), 4);
    })

    it('return proper power of negative number', () => {
        assert.equal(power(-2, 1), -2);
    })

    it('return proper power of negative number', () => {
        assert.equal(power(-2, 2), 4);
    })
     
    it('return proper result of 0 pow', () => {
        assert.equal(power(2, 0), 1);
    })

    it('return proper result of 1 pow', () => {
        assert.equal(power(2, 1), 2);
    })
})