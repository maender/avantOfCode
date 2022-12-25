from collections import deque
import sys

import heapq

def heuristic(pos, end):
	# calculate the Manhattan distance between the current position and the end position
	row_distance = abs(pos[0] - end[0])
	col_distance = abs(pos[1] - end[1])
	return row_distance + col_distance

def find_shortest_path(heightmap, start, end):
	# create a priority queue to store the squares to be visited
	queue = []
	heapq.heappush(queue, (0, start))
	# create a set to keep track of visited squares
	visited = set()
	
	# initialize the distance to the starting position as 0
	distance = {start: 0}
	
	# create a mapping of directions to offsets for row and column
	directions = {
		'up': (0, -1),
		'down': (0, 1),
		'left': (-1, 0),
		'right': (1, 0)
	}
	
	while queue:
		# get the next square to visit
		_, (col, row) = heapq.heappop(queue)
		
		# if we have reached the destination, return the distance
		# print(col, row)
		if (col, row) == end:
			print(f"Path found, dist: {distance[(col, row)]}")
			return distance[(col, row)]
		
		# mark the current square as visited
		visited.add((col, row))
		
		# get the elevation of the current square
		current_elevation = heightmap[row][col]
		
		# print(queue, visited, distance)
		# input()
		# visit each of the four adjacent squares
		for _, (dcol, drow) in directions.items():
			# calculate the row and column of the adjacent square
			next_row, next_col = row + drow, col + dcol
			# skip the square if it is out of bounds or has already been visited
			if (next_row < 0 or next_row >= len(heightmap) or
					next_col < 0 or next_col >= len(heightmap[0]) or
					(next_col, next_row) in visited):
				continue
			
			# get the elevation of the adjacent square
			next_elevation = heightmap[next_row][next_col]
			
			# skip the square if the elevation is more than 1 higher than the current elevation
			if next_elevation - current_elevation > 1:
				continue
			
			# calculate the new distance to the adjacent square
			new_distance = distance[(col, row)] + 1
			
			# update the distance to the adjacent square if it is shorter than the current distance
			if (next_col, next_row) not in distance or new_distance < distance[(next_col, next_row)]:
				distance[(next_col, next_row)] = new_distance
				priority = new_distance + heuristic((next_col, next_row), end)
				heapq.heappush(queue, (priority, (next_col, next_row)))
			
	# if we have reached this point, it means we have not found the destination
	return -1


if __name__ == '__main__':
	grid = []
	with open('resources/day12', 'r') as f:
		for i, line in enumerate(f.readlines()):
			if 'S' in line:
				start = (line.find('S'), i)
			if 'E' in line:
				end = (line.find('E'), i)
			grid.append([ord(x) if x != 'S' and x != 'E' else ord('a') if x == 'S' else ord('z') for x in line.replace('\n', '')])
	# for line in grid:
	# 	print(line)
	print(start, end)
	dists = []
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] == 97:
				dists.append(find_shortest_path(grid, (x, y), end))
	dists.sort()
	print(dists)