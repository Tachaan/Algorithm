# 感想
high-votedは探索を最後まで左右比較をやるようにしている。、探索限界が答えという形になっている。
探索限界まで行くと、left == rightになるため、nums[left] == nums[right] が答えとなる
比較もmidとightのみで見ている。