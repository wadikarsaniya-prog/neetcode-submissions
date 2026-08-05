class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        count = 0
        fleet_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > fleet_time:
                count += 1
                fleet_time = time

        return count