# SkyHigh Adventures Travel Cost Calculator

## Overview
A Python program for calculating family vacation costs with destination-based pricing and dynamic discounts.

## Project Details
**Course:** RCIT 1763 – Object-Oriented Programming
**Semester:** July 2024
**Submission Date:** 5 October 2024

## Features
- Multiple family vacation cost calculation
- Destination options:
  1. Grand Canyon
  2. Yellowstone National Park
  3. Glacier National Park
- Applies tiered discounts for adults and children
- Converts final costs to Malaysian Ringgit (MYR)

## Destinations
| Option | Destination | Transportation | Accommodation |
|--------|-------------|----------------|---------------|
| 1 | Grand Canyon | USD 200 | USD 1,500 |
| 2 | Yellowstone National Park | USD 180 | USD 1,700 |
| 3 | Glacier National Park | USD 220 | USD 1,600 |

## Discount Structure
### Accommodation Discounts
- 1 adult: No discount
- 2 adults: 15% discount per adult
- 3+ adults: 25% discount per adult
- Children: 40% discount

### Transportation Discounts
- Adults: No discount
- Children: 50% discount

## Prerequisites
- Python 3.7+

## Usage
```bash
python travel_agency_script.py
```

1. Enter family name
2. Select destination (1-3)
3. Input number of adults
4. Input number of children
5. Repeat for multiple families or type 'quit' to finish

## Sample Output
```
Total cost for Smith family: MYR 12,345.67
```

## Key Concepts
- User input validation
- Nested dictionaries
- Cost calculation algorithms
- Currency conversion

## Contributing
Improvements and suggestions welcome!

## Academic Integrity
This is an individual assignment. Ensure you understand and comply with academic honesty guidelines.

## License
[Choose an appropriate license]
