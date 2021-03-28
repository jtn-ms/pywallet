#!/usr/bin/env python
from __future__ import absolute_import
# LOST FIRST,
# IF YOU SCARED OF LOSING, YOU LOSE MORE.
# YOU WILL GAIN WHAT YOU WANT IF NOTHING IS MEANINGFUL TO YOU.
# NO FEELING, NOTHING AFRAID
# 该去去，该来的来，何必高兴，何必伤心
#######################################################
# ALL-IN(背水一战): 死去获得重生, 1到10, 我经过好几次(5次以上)做过没有退路的赌博.
# 获得一切,失去一切. 人生如一场戏. 0.1,0.3,0.6,0.9,1.1(0.5,0.1.2 fail)
# 大起大落, 喜怒哀乐, 失败与成功，我经验的每场赌博想活不同的人的人生一样
# 一个礼拜的时间过去了但好像几年过去一样，思考的多，失去的多，懂得多
#　起死回生－人生一次体验就够了．我现在很累．
# 现在满足的话，我回停在这儿．永远得不到我想要的．
# 但我现在没有继续做下去的勇气和力气．我需要休息．
# 每个事情都是需要认真对待，才有结果．赌博也不是玩儿的．玩儿的就是你的命
# 回避会失去更多．需要勇敢面对．
# 不能控制频率的话，你永远得不到你所想得.
# NO PAIN, NO GAIN
# [PROBLEM]
# BLOCK HASH IS KINDS OF RANDOM NUMBER, UNPREDICTABLE
# REVEAL IS CLOSED, MAYBE TIME_BASED ALSO UNPREDICTABLE
# COMMIT - YOU CAN CHECK IT TX DATA IN METAMASK BEFORE YOU COMFIRM TRANSACTION
# BUT COMMIT IS SHA3(REVEAL), SO YOU CAN'T PREDICT IT.
# WHERE REAL RNG IS BLOCK HASH & NUMBER. EVEN THOUGH YOU PUT HIGHEST FEE ON YOUR TX
# SITLL YOU HAVE NO IDEA WHICH BLOCK NUMBER & HASH WILL BE FOR YOU.
#############################################################
# [ATTITUDE]
# USE BEGINNER'S LUCK
# REFRESH YOUR MIND. MAKE SURE YOU ATTEND THE GAME AS A BEGINNER.
# FORGET ABOUT WHAT YOU EARN, WHAT YOU LOSE.
# NEVER INCREASE YOUR BET EVEN THOUGH YOU KEEP WINNING.
# DOUBLE & TRIPLE IS LUCK, FIVETIMES IS GRADUATION SIGNAL.
# EVERYTHING IS NOTHING MORE THAN NUMBER. DO IT JUST LIKE PLAYING GAME.
# KEEP THE RULE, COOLIFY YOUR HEAD.
# YOU CAN WIN OR YOU CAN LOSE. JUST EMBRACE WHATEVER THE RESULT IS.
# DON"T BELIEVE ANY MIRACLE. TREAT YOUR LUCK CAUTIOUSLY.
# DON"T BREAK YOUR RHYTHM. KEEP STABLE, CAUTIOUS, MATURE
# I NEED TO ACCOMPLISH PSYCHOLOGICAL MATURITY.
# YOU SHOULD KILL YOURSELF FIRST BEFORE YOU WANT TO BECOME SOMEBODY.
# YOU CAN"T ACHIEVE YOUR OBJECTIVE OVERNIGHT. NEVER HASTE.
# [BAD SIGNAL]
# OVERNIGHT GAMING, STOP GAMING MIDNIGHT
# LATE RESPONSE OF settleBet Tx
# WIN RATE IS UNDER 50%(FIRST FAIL, SECOND FAIL)
#############################################################
# [QUIT CONDITION]
# TEST THE DAY's LUCK. MAKE DECISION ACCORDING TO IT, KEEP PLAYING OR QUITING
# IF BEGINNER's LUCK DOESN't WORK, I QUIT
# IF WIN RATE IS UNDER 50%, I QUIT
# ONCE LOSE, ABANDON THE ACCOUNT
# BELIEVE YOUR FIRST THOUGHT. IF ANY BAD FEELING, QUIT
# NEVER RETURN BEFORE FORGET ALL. REFRESH YOUR MIND CLEARLY
#############################################################
# DEAL WITH DEVIL
# IF YOU WANT TO BECOME SOMEONE, YOU SHOULD KILL YOURSELF AS BORN FIRST.
# IF THE GAME DEFEATS ALL HUMAN, YOU SHOULD HAVE NON-HUMAN MIND & HEART(NO HEART).
# EMPTY YOUR MIND, INNER PEACE, BALANCE BETWEEN VANITY & SANITY, BRACE YOURSELF
# FIND YOUR RHYTHM & FREQUENCY
# COLD HEART, EVERTHING IS NOTHING MORE THAN NUMBER. WIN OR LOSE
# TRY, REJECT, CONFIRM
# NOTHING FREE, YOU HAVE TO PAY FOR IT.
# I JUST BORROW IT, SOMEDAY I WILL RETURN IT BACK.
# IF YOU ARE THE SELECTED, YOU WILL HAVE TO SERVE.
# YOU CAN'T BE FREE FROM EVERTHING.
# QUIT CONDITION SHOULD BE PRESETTLED.
# KEEP ORIGIN
###############################################
# [TAcTIc]
# 1 2 5 10 20 50 ...
# 3**(0,1,2,3,4,5,6,7,8,...)
# 1 3 9 27 81 ((1+3+9+27+81)*2+1)....
# 0.1,0.3,0.6,0.9,1.1(0.5,1.2 failed)
# Frequency: BET AMOUNT, IP LOCATION, INTERVAL
# 背水一战: ALL-IN
# 走为上： 遇到危险（LOSE）,跑（ABANDON THE ACCOUNT）　
# 游击战： MAKE SURE NO ONE RECOGNIZE YOU. GAIN SMALL & RETREAT, BUT COME BACK AGAIN.
# 抛砖引玉,李代桃僵: WIN OVER BIG, LOSE OVER SMALL. IT MAKES YOU ALWAYS EARN. AND ALSO DON'T BREAK GOD's RULE
############################################################
# YOU ARE NOTHING MORE THAN FISH. THEY LURE YOU INTO THE TRAP
# IF YOU ARE ENOUGH CUNNING TO STEAL THE BAIT WITHOUT BEING TRAPPED,
# YOU CAN SURVIVE ON THEIR FEED.
#########################################################################   |
# [FISHING GAME]                                                            |    
# FISHMAN BAIT A TRAP, I AM A CUNNING FISH.                                  \_
# I STEAL BAIT WITHOUT BEING TRAPPED                                           \_ 
# BIG FISH EAT SMALL FISH                                               ^        |   
# I GROW MYSELF SECRETLY. MAKE SURE NO ONE KNOWS OF YOUR EXISTENCE.      \      /
# TRAVEL MUCH, TARGET MANY,                                                \___/
# SHRIMP->JELLYFISH->CATFISH->OCTOPUS->SHARK->WHALE->HOMO->GOD
# EAT BAIT, AVOID HOOK
# SENSING DANGER, DISAPPEAR
# ATTACK WEAK, AVOID STRONG
######################################
# [LURE]
# FOR FISHING - HOOK, NET
# FOR HUNTING - TRAP
#########################################
# [FreQenCy]
# Frequency Is God
# WHEN
# HOW OFTEN
# HOW MANY
# HOW MUCH
# WHERE
# WHAT(doesn't matter, control your mind, I always bet on small. That represents my promise for good purpose.)
# [CAUTION]
# POWER IS HARD TO AVOID. WHEN IT COMES, IT WILL AWAKE YOU.
MAX_MASK_MODULO = 100#dice:6, coin flip:2
MAX_BET_MASK = 2 ** MAX_MASK_MODULO
POPCNT_MULT = int("0000000000002000000000100000000008000000000400000000020000000001",16)
POPCNT_MASK = int("0001041041041041041041041041041041041041041041041041041041041041",16)
POPCNT_MODULO = int("3F",16)

MIN_BET = 0.01
MAX_AMOUNT = 300000

bet=dict()

# amount: 0.1 ~ 300000
# mask:   1234:1111(0xf),125:10011(0x13),123:111(0x7)
# modulo: 2,6,36,100  
# rollUnder: 0 ~ 63(related to reward, not critical in most cases)
#####################################
# blkhash: block number when committing
# commitblknum(cblknum) > block.number for signer checking
# placeblknum(pblknum) = block.number for betting
# blkhash = blockhash
#####################################
# commit/reveal: bet index,generated by platform,THIS IS THE KEY, RNG
# commit = keccak256(reveal)
# reveal->commit, reveal != commit
# reveal+blockhash->entropy->dice
# where blockhash is when commiting placeBet or settleBet
# pblockhash when placing bet
# reveal is completely controlled by PLATFORM
# blockhash is also PREDICTABLE
# In conclusion, the result is controllable by HOUSE
# GAMBLER ONLY SELECT WHEN(pblkhash), BUT THE HOUSE CONTROL REVEAL
# BUT HOUSE ALSO HAS LIMITED TIME, ALSO HARD TO PREDICT THE RESULT OF HASH
#####################################
# entropy: keccak256(reveal,pblkhash)
# dice:   0 ~ modulo(entropy%modulo)
# 2**dice: 000001,000010,000100,001000,010000,100000
# WIN DETECT: (0,!0)2**dice & mask
###################################
# pblock.number <= commitLastBlock
# h=keccak256(commitLastBlock,commit)
# v, r, s = ecsign(h,privkey)
# privkey2addr(privkey) == secretSigner = ecrecover(h,v,r,s)
####################################
# Only Croupier/Dealer has priviledge to disclose the bet result
# commit for secretSigner
def commitBet(amount,mask,modulo,blkhash,reveal):

    # placeBet
    assert modulo > 1 and modulo < MAX_MASK_MODULO
    assert amount > MIN_BET and  amount < MAX_AMOUNT
    assert mask > 0 and mask < MAX_BET_MASK
    rollUnder=((mask*POPCNT_MULT)&POPCNT_MASK) % POPCNT_MODULO
    # print("rollUnder: {0}".format(rollUnder))
    diceWinAmount,jackpotFee = getDiceWinAmount(amount, modulo, rollUnder)
    # print("diceWinAmount: {0},jackpotFee: {1}".format(diceWinAmount,jackpotFee))
    # settleBet, settleBetCommon
    dice = roll(modulo,reveal,blkhash)
    isWin=determine(modulo,dice,mask,rollUnder)
    diceWin,jackpotWin=0,0
    if isWin: print("You Win!!!!");diceWin=diceWinAmount
    else: print("You Lose!!!!")
    print("diceWin: {0},jackpotWin: {1}".format(diceWin,jackpotWin))
    return isWin

def roll(modulo,reveal,blkhash):
    from sha3 import keccak_256
    from ethereum.abi import encode_single,encode_abi
    encoded = encode_abi(('uint256','bytes32'),(long(reveal,16),blkhash.decode("hex")))
    # print("encoded: {0}".format(encoded.encode('hex')))
    entropy=keccak_256(encoded).hexdigest()
    # print("entropy: {0}".format(entropy))
    dice = int(entropy,16) % modulo
    # print("dice: {0}/0~5".format(dice))
    return dice

def determine(modulo,dice,mask,rollUnder):
    if modulo <= MAX_MASK_MODULO:
        binbet =bin(mask)[2:]
        bindice=bin(2**dice)[2:]
        print("your bet:{0}-{1}".format((modulo-len(bindice))*'0'+bindice,\
                                        (modulo-len(binbet))*'0'+binbet))
        if ((2 ** dice) & mask) != 0:
            return True
    elif dice < rollUnder:
        return True
    return False

JACKPOT_FEE = 0.001
JACKPOT_MODULO = 1000
MIN_JACKPOT_BET = 0.1
HOUSE_EDGE_MINIMUM_AMOUNT = 0.0003
HOUSE_EDGE_PERCENT = 1
def getDiceWinAmount(amount, modulo, rollUnder):
    assert 0 < rollUnder and rollUnder < modulo
    jackpotFee = JACKPOT_FEE if amount >= MIN_JACKPOT_BET else 0
    houseEdge = amount * HOUSE_EDGE_PERCENT / 100
    if houseEdge < HOUSE_EDGE_MINIMUM_AMOUNT:
        houseEdge = HOUSE_EDGE_MINIMUM_AMOUNT
    assert houseEdge + jackpotFee <= amount
    winAmount = (amount - houseEdge - jackpotFee) * modulo / rollUnder
    return winAmount,jackpotFee

# mask:   0000000000000000000000000000000000000000000000000000000000000007
# modulo: 0000000000000000000000000000000000000000000000000000000000000006
# pblknum:
# reveal: 
### cblknum: 0000000000000000000000000000000000000000000000000000000000b75bae
### commit: 3cc363a74120d0c5fd7f9ba1ca1d77288080fe83a369489dcab541a0c0a34a04
### r:  a1b3db60f50fe3ba70b33a4a801ff2852a8665e151a1199c398a86fcb34c30f0
### s:  af817fa334c20f46ff98c5bc3af4752741301e61a011ffac81ce153f3b87e70e
def test_one():
    amount = 0.1
    mask   = "0000000000000000000000000000000000000000000000000000000000000015"
    modulo = "0000000000000000000000000000000000000000000000000000000000000006"
    reveal = "79ca8d1e967a7232e4d40de4c073da5d758cc2a7f86bda2229e3ac7e1f69a5c4"
    nmask = int(mask,16)
    nmodulo = int(modulo,16)
    npblknum = 12024062 
    commitBet(amount,nmask,nmodulo,npblknum,reveal)

def getcurtime():
    import time
    return round(time.time() * 1000)

def genMask(modulo):
    # print("modulo: {0}".format("1"*modulo))
    ### 123
    # print("modulo: {0}".format("000111"))
    return int("000111",2)

# mask   = "000000000000000000000000000000000000000000000000000000000000000f"
# modulo = "0000000000000000000000000000000000000000000000000000000000000006"
try:
    from eth.etherscan import getBlockHash
except:
    from etherscan import getBlockHash
def simOne(mask="000111"):
    # blkhash
    print("#"*50)
    pblknum,blkhash=getBlockHash("latest")
    assert blkhash != ''
    blkhash = blkhash[2:] if '0x' in blkhash else blkhash
    amount = 0.25
    nmodulo = 6
    # mask
    nmask = int(mask,2)
    # reveal
    from sha3 import keccak_256
    now = int(getcurtime())
    reveal = keccak_256(bytes(now)).hexdigest()
    # commit
    print("modulo: {0}-{1}".format("1"*nmodulo,nmodulo))
    print("mask:   {0}-{1}".format(mask,nmask))
    print("blkhash: {0}".format(blkhash))
    print("reveal: {0}".format(reveal))
    print("amount: {0}".format(amount))
    return commitBet(amount,nmask,nmodulo,blkhash,reveal)

def simMany(times=10):
    winCount = 0
    for i in range(times):
        if simOne(): winCount+=1
    print("win-{0}/{1}".format(winCount,times))

if __name__ == "__main__":
    # test_losecase()
    # test_wincase1()
    simMany()
