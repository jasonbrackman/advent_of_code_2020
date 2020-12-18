import helpers


def do_work(nums, max_num):
    visited = dict()
    last_num = None
    for i in range(1, max_num + 1):
        if len(nums) >= i:
            r = nums[i - 1]
            if r not in visited:
                visited[r] = [i]
            else:
                visited[r].append(i)
            last_num = r

        elif last_num in visited and len(visited[last_num]) == 1:
            visited[0].append(i)
            last_num = 0

        else:
            a, b = visited[last_num][-1], visited[last_num][-2]
            r = a - b
            if r not in visited:
                visited[r] = [i]
            else:
                visited[r].append(i)
            last_num = r

    return last_num


def run():
    lines = helpers.get_lines(r"./data/day_15.txt")
    nums = [int(i) for line in lines for i in line.split(",")]
    assert do_work(nums, 2020) == 475
    assert do_work(nums, 30_000_000) == 11261


if __name__ == "__main__":
    run()
