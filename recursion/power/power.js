// power(2,0) // 1
// power(2,2) // 4
// power(2,4) // 16

function power(num, pow) {
    let result = 1;

    function helper(num, pow) {
        if (pow === 0) return;
        result *= num;
        pow--;

        helper(num, pow)
    }

    helper(num, pow);

    return result;
}

export { power }