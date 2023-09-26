class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - pos) / spd for pos, spd in cars]
        front = 0
        fleet = 0
        for t in times:
            if t > front:
                fleet += 1
                front = t
        return fleet
