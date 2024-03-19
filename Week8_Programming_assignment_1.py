def create_points_table(matches):
    points_table = {}
    
    for match in matches:
        for team in match:
            points_table[team] = 0

    for match in matches:
        winner = match[0]
        for opponent in match[1:]:
            points_table[winner] += 1

    sorted_table = sorted(points_table.items(), key=lambda x: (-x[1], x[0]))
    for team, points in sorted_table:
        print(f"{team}:{points}")

matches = [
    input().split(',') for _ in range(8)
]
create_points_table(matches)
