LOOP_CNT = 4;
(START_R, START_C, START_DIR) = (0, 0, 0);
DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));
(LEFT_VEC, RIGHT_VEC) = ((2, 3, 1, 0), (3, 2, 0, 1));

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        (curR, curC, curDir) = (START_R, START_C, START_DIR);
        
        for loopIdx in range(LOOP_CNT):
            for curInstruction in instructions:
                if (curInstruction == "G"):
                    (curR, curC) = (curR + DIR_VEC[curDir][0], curC + DIR_VEC[curDir][1]);
                elif (curInstruction == "L"):
                    curDir = LEFT_VEC[curDir];
                elif (curInstruction == "R"):
                    curDir = RIGHT_VEC[curDir];
                
            if ((curR, curC, curDir) == (START_R, START_C, START_DIR)):
                return True;

        return False;
