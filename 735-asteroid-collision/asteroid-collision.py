class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for asteroid in asteroids:
            flag = True
            while st and st[-1] > 0 and asteroid < 0:
                if abs(st[-1]) < abs(asteroid):
                    st.pop()
                    continue
                elif abs(st[-1]) == abs(asteroid):
                    st.pop()
                flag = False
                break

            if flag:
                st.append(asteroid)

        return st
