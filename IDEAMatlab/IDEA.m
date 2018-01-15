% IDEA encryption
key = 'ABCDEFGHIJKLMNOP';
keyA = uint8(key);

plaintext = 'Hello! This is my secret message.';
pB = uint8(dec2bin(plaintext,8));
[y x] = size(pB);
pb2 = [];
line = [];
for i = 1:floor(y/4)
    line = [line pB(i,:)];
end
pb2(1,:) = line;
line = [];
for i = floor(y/4)+1:floor(y/2)
    line = [line pB(i,:)];
end
pb2(2,:) = line;
line = [];
for i = floor(y/2)+1:floor(y/4)+floor(y/2)
    line = [line pB(i,:)];
end
pb2(3,:) = line;
line = [];
for i = (floor(y/4)+ceil(y/2)+1):y
    line = [line pB(i,:)];
end
pb2(4,:) = line;
line = [];

pb2 = mod(pb2,2);
pb2 = [1;2;3;4];
keyB = reshape(keyA.',1,[]);
kc = 0;

[k1 k2 k3 k4 k5 k6 k7 k8] = Keys(keyB,kc);
keys = [k1 k2 k3 k4 k5,k6 k7 k8];
%%IDEA ROUND
C = 1;
for nn = 1:8
    %PreRound
    if(C == 8)
        kc = kc+1;
        [k1 k2 k3 k4 k5 k6 k7 k8] = Keys(keyB,kc);
    keys = [k1 k2 k3 k4 k5,k6 k7 k8];
        C = 1;
    end
    t1 = (keys(C));
    C = C+1;
    if(C == 8)
        kc = kc+1;
        [k1 k2 k3 k4 k5 k6 k7 k8] = Keys(keyB,kc);
    keys = [k1 k2 k3 k4 k5,k6 k7 k8];
        C = 1;
    end
    if t1 == 0
       t1 = 2^16;
    end
    if pb2(1) == 0
        pb2(1) = 2^16;
    end
    a = (mod(t1*pb2(1),2^16+1));
    if a == 2^16
        a = 0;
    end
    t2 = (keys(C));
    C = C+1;
    if(C == 8)
        kc = kc+1;
        [k1 k2 k3 k4 k5 k6 k7 k8] = Keys(keyB,kc);
        keys = [k1 k2 k3 k4 k5,k6 k7 k8];
        C = 1;
    end
    b = (mod(t2+pb2(2),2^16));
    t3 = (keys(C));
    C = C+1;
    if(C == 8)
        kc = kc+1;
        [k1 k2 k3 k4 k5 k6 k7 k8] = Keys(keyB,kc);
        keys = [k1 k2 k3 k4 k5,k6 k7 k8];
        C = 1;
    end
    c = (mod(t3+pb2(3),2^16));
    t4 =(keys(C));
    C = C+1;
    if(C == 8)
        kc = kc+1;
        [k1 k2 k3 k4 k5 k6 k7 k8] = Keys(keyB,kc);
        keys = [k1 k2 k3 k4 k5,k6 k7 k8];
        C = 1;
    end
    d = (mod(t4*pb2(4),2^16+1));
    %L1
    t5 = bitxor(a,c);
    t6 = bitxor(b,d);
    %L2
    t7 = mod(t5*(keys(C)),2^16+1);
    t8 = mod(t7+t6,2^16);
    C = C+1;
    if(C == 8)
        kc = kc+1;
        [k1 k2 k3 k4 k5 k6 k7 k8] = Keys(keyB,kc);
        keys = [k1 k2 k3 k4 k5,k6 k7 k8];
        C = 1;
    end
    %L3
    t9 = mod(t8*keys(C),2^16+1);
    t10 = mod(t9+t7,2^16);
    C = C+1;
    if(C == 8)
        kc = kc+1;
        [k1 k2 k3 k4 k5 k6 k7 k8] = Keys(keyB,kc);
        keys = [k1 k2 k3 k4 k5,k6 k7 k8];
        C = 1;
    end
    %L4
    b = bitxor(t9,c);
    a = bitxor(t9,a);
    %L5
    c = bitxor(t10,b);
    d = bitxor(t10,d);
end
a
b
c
d 