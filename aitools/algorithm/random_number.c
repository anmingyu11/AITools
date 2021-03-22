// https://en.wikipedia.org/wiki/Linear_congruential_generator
int rand(seed){
    // 生成一个随机数
    // 64位整数
    next_random = next_random * (unsigned long long)25214903917 + 11;

    // 如果 随机数 > ran ，丢弃该词。
    //
    // (next_random & 0xFFFF) 抽取 next_random 的低16位随机数。
    // 将这个数除以 65536 (2^16) 给我们一个 (0,1) 的分数。
    // 所以这段代码只是生成一个随机分数。
    if (ran < (next_random & 0xFFFF) / (real)65536) continue;
}