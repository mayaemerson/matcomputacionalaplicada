import math
import os
from typing import List, Set, Callable
import matplotlib.pyplot as plt

class MathematicalFunction:
    """
    Represents a mathematical function f: X -> Y mapping a domain to a codomain.
    """
    def __init__(self, domain: Set[float], codomain: Set[float], mapping: Callable[[float], float]):
        self.domain = domain
        self.codomain = codomain
        self.mapping = mapping

    def calculateImageSet(self) -> Set[float]:
        """
        Calculates the image set of the function based on its finite domain.
        """
        imageSet = set()
        for x in self.domain:
            y = self.mapping(x)
            if y in self.codomain:
                imageSet.add(y)
        return imageSet


class ContinuousExponentialGrowth(MathematicalFunction):
    """
    Models continuous exponential growth of the form U(t) = U0 * e^(k * t),
    which is a specific type of mathematical function mapping time to quantity.
    """
    def __init__(self, initialValue: float, continuousRate: float, timeDomain: Set[float]):
        self.initialValue = initialValue
        self.continuousRate = continuousRate
        
        # Define mapping: U(t) = U0 * e^(k * t)
        super().__init__(
            domain=timeDomain,
            codomain=set(),  # Infinite codomain for positive real numbers
            mapping=lambda t: self.initialValue * math.exp(self.continuousRate * t)
        )

    def calculateAtTime(self, time: float) -> float:
        """
        Computes f(t) for a single specific time value.
        """
        return self.mapping(time)

    def simulateTimeline(self, sortedTimeSteps: List[float]) -> List[float]:
        """
        Simulates and prints the exponential growth over a series of steps.
        Returns the calculated values.
        """
        calculatedValues = []
        print(f"Exponential Growth Simulation (U0={self.initialValue}, k={self.continuousRate})")
        print("=" * 60)
        print(f"{'Time (t)':<12} | {'Exact Value U(t)':<20} | {'Rounded Value':<15}")
        print("-" * 60)
        for t in sortedTimeSteps:
            exactValue = self.calculateAtTime(t)
            calculatedValues.append(exactValue)
            roundedValue = math.floor(exactValue)
            print(f"{t:<12.1f} | {exactValue:<20.4f} | {roundedValue:<15}")
        print("=" * 60)
        return calculatedValues


class GrowthVisualizer:
    """
    Handles plotting and visualization of mathematical growth functions.
    """
    @staticmethod
    def plotUserGrowth(timeSteps: List[float], userCounts: List[float], outputPath: str) -> None:
        """
        Generates a premium stylized chart representing the user growth curve over time.
        """
        # Set modern layout styling
        plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
        
        fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
        
        # Customize curve style
        ax.plot(timeSteps, userCounts, color='#007acc', linewidth=2.5, zorder=3, label='Exponential Growth U(t)')
        ax.fill_between(timeSteps, userCounts, color='#007acc', alpha=0.1)
        
        # Draw and style key milestone coordinates
        initialTime, initialUsers = timeSteps[0], userCounts[0]
        finalTime, finalUsers = timeSteps[-1], userCounts[-1]
        
        ax.scatter([initialTime], [initialUsers], color='#d9534f', s=100, zorder=5, label=f'Initial: {int(initialUsers)} users')
        ax.scatter([finalTime], [finalUsers], color='#5cb85c', s=100, zorder=5, label=f'Target (t=12): {int(finalUsers)} users')
        
        # Add labels to major milestones
        ax.annotate(f"U(0) = {int(initialUsers)}", (initialTime, initialUsers), textcoords="offset points", 
                    xytext=(15, -5), ha='left', fontsize=10, fontweight='bold', color='#333333')
        ax.annotate(f"U(12) = {int(finalUsers)}", (finalTime, finalUsers), textcoords="offset points", 
                    xytext=(-15, 15), ha='right', fontsize=10, fontweight='bold', color='#333333')
        
        # Setup grid and layout boundaries
        ax.set_title("User Growth Simulation over 12 Months\nFormula: U(t) = U0 * e^(k * t)", fontsize=14, fontweight='bold', pad=15)
        ax.set_xlabel("Time (Months)", fontsize=12, labelpad=10)
        ax.set_ylabel("Number of Users", fontsize=12, labelpad=10)
        
        # Refined legend positioning
        ax.legend(loc='upper left', frameon=True, facecolor='#ffffff', edgecolor='#cccccc', framealpha=0.9)
        plt.tight_layout()
        
        # Save output image
        plt.savefig(outputPath, bbox_inches='tight')
        plt.close()
        print(f"\nStylized chart saved successfully at: {outputPath}")


if __name__ == "__main__":
    # Domain representing months from 0 to 12
    monthsDomain = {float(m) for m in range(13)}
    
    # Study Case: 1000 initial users, k = 0.05, 12 months timeline
    growthModel = ContinuousExponentialGrowth(
        initialValue=1000.0,
        continuousRate=0.05,
        timeDomain=monthsDomain
    )
    
    # Run simulation using sorted timeline steps
    timeline = sorted(list(monthsDomain))
    results = growthModel.simulateTimeline(timeline)
    
    # Exact validation check for t = 12
    targetMonth = 12.0
    result = growthModel.calculateAtTime(targetMonth)
    print(f"Verification: U({targetMonth:.0f}) = {result:.4f} (~ {math.floor(result)} users)")
    
    # Generate and save modern chart
    currentDir = os.path.dirname(os.path.abspath(__file__))
    chartPath = os.path.join(currentDir, "user_growth.png")
    GrowthVisualizer.plotUserGrowth(timeline, results, chartPath)
