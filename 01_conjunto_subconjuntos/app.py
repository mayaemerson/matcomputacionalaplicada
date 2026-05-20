import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import Set, FrozenSet, Any, List

class SetTheoryToolbox:
    """
    Utility class implementing fundamental mathematical operations
    and relations of Set Theory.
    """
    @staticmethod
    def belongsTo(element: Any, targetSet: Set[Any]) -> bool:
        """
        Checks membership relation (x in A).
        """
        return element in targetSet

    @staticmethod
    def isSubset(setA: Set[Any], setB: Set[Any]) -> bool:
        """
        Checks subset inclusion relation (A subset-of-or-equal B).
        """
        return setA.issubset(setB)

    @staticmethod
    def isProperSubset(setA: Set[Any], setB: Set[Any]) -> bool:
        """
        Checks proper subset inclusion relation (A subset-of B and A != B).
        """
        return setA.issubset(setB) and setA != setB

    @staticmethod
    def getPowerSet(targetSet: Set[Any]) -> List[FrozenSet[Any]]:
        r"""
        Generates the Power Set P(A) of a given set A.
        Returns a list of frozen sets representing all subsets.
        """
        elements = list(targetSet)
        powerSetList = []
        n = len(elements)
        # There are 2^n subsets
        for i in range(1 << n):
            subset = frozenset(elements[j] for j in range(n) if (i & (1 << j)))
            powerSetList.append(subset)
        return powerSetList


class FeedAlgorithmSimulation:
    """
    Simulates a social media feed personalization using set intersections
    and subsets as discussed in analisematematicacaos.pdf.
    """
    def __init__(self, userInterests: Set[str], friendEngagements: Set[str], allPosts: Set[str]):
        self.userInterests = userInterests
        self.friendEngagements = friendEngagements
        self.allPosts = allPosts

    def generateFeed(self) -> Set[str]:
        """
        Personalizes the feed by calculating the intersection of user interests
        and contents engaged by friends (UserInterests intersect FriendEngagements).
        """
        return self.userInterests.intersection(self.friendEngagements)

    def generateVisualization(self, outputPath: str = "feed_venn_diagram.png") -> None:
        """
        Plots a stylized Venn diagram representing the feed intersection
        and saves it as an image.
        """
        fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
        
        # Set premium background color
        fig.patch.set_facecolor('#f7f9fc')
        ax.set_facecolor('#f7f9fc')
        
        # Draw user circle (Left)
        circleUser = patches.Circle((-1.0, 0), 2.0, color='#3b82f6', alpha=0.4)
        # Draw friends circle (Right)
        circleFriends = patches.Circle((1.0, 0), 2.0, color='#ec4899', alpha=0.4)
        
        ax.add_patch(circleUser)
        ax.add_patch(circleFriends)
        
        # Adjust plot limits and aspect ratio
        ax.set_xlim(-4, 4)
        ax.set_ylim(-3, 3)
        ax.set_aspect('equal')
        
        # Remove axes for clean diagram view
        ax.axis('off')
        
        # Text descriptions inside the circles
        # User interests exclusive to the user (U \ F)
        userExclusive = self.userInterests.difference(self.friendEngagements)
        userText = "\n".join(sorted(list(userExclusive)))
        ax.text(-2.0, 0, f"Interesses do Usuário\n\n{userText}", ha='center', va='center', color='#1e3a8a', fontsize=9, weight='bold')
        
        # Friends engagements exclusive to friends (F \ U)
        friendExclusive = self.friendEngagements.difference(self.userInterests)
        friendText = "\n".join(sorted(list(friendExclusive)))
        ax.text(2.0, 0, f"Engajamento de Amigos\n\n{friendText}", ha='center', va='center', color='#9d174d', fontsize=9, weight='bold')
        
        # Personalized Feed (U intersect F)
        feedItems = self.generateFeed()
        feedText = "\n".join(sorted(list(feedItems)))
        ax.text(0, 0, f"Interseção do Feed\n(U ∩ F)\n\n{feedText}", ha='center', va='center', color='#111827', fontsize=9, weight='bold')
        
        # Chart titles
        plt.title("Modelo de Diagrama de Venn do Feed de Redes Sociais", fontsize=13, weight='bold', color='#1f2937', pad=20)
        
        isProper = SetTheoryToolbox.isProperSubset(feedItems, self.allPosts)
        plt.figtext(0.5, 0.05, f"O feed personalizado é um subconjunto próprio de todas as postagens? {isProper}", 
                    ha='center', fontsize=9, color='#4b5563', style='italic')
        
        plt.tight_layout()
        plt.savefig(outputPath, bbox_inches='tight', facecolor=fig.get_facecolor())
        plt.close()


if __name__ == "__main__":
    # Define system sets
    allAvailablePosts = {
        "Notícias de Tecnologia", "Memes de Gatos", "Física Quântica", "Receitas de Culinária", 
        "Dicas de Treino", "Vlogs de Viagem", "Novidades de Jogos", "Política Local"
    }
    
    userInterests = {"Notícias de Tecnologia", "Física Quântica", "Memes de Gatos", "Novidades de Jogos"}
    friendEngagements = {"Memes de Gatos", "Receitas de Culinária", "Novidades de Jogos", "Vlogs de Viagem"}
    
    # 1. Instantiating the Toolboxes
    print("=== Estudo de Teoria dos Conjuntos e Relações ===")
    
    # Pertinance checks
    print(f"O elemento 'Notícias de Tecnologia' pertence aos Interesses do Usuário? {SetTheoryToolbox.belongsTo('Notícias de Tecnologia', userInterests)}")
    print(f"O elemento 'Receitas de Culinária' pertence aos Interesses do Usuário? {SetTheoryToolbox.belongsTo('Receitas de Culinária', userInterests)}")
    
    # Inclusion/Subsets checks
    print(f"Os Interesses do Usuário são um subconjunto de Todas as Postagens? {SetTheoryToolbox.isSubset(userInterests, allAvailablePosts)}")
    
    # Power Set demonstration (using a smaller set for readability)
    sampleSet = {"Notícias de Tecnologia", "Memes de Gatos"}
    print(f"\nConjunto das Partes de {sampleSet}:")
    for idx, subset in enumerate(SetTheoryToolbox.getPowerSet(sampleSet)):
        print(f" Subconjunto {idx + 1}: {set(subset)}")
        
    # 2. Simulating Social Media Feed (Intersection)
    simulation = FeedAlgorithmSimulation(userInterests, friendEngagements, allAvailablePosts)
    feed = simulation.generateFeed()
    
    print("\n=== Simulação de Feed de Redes Sociais ===")
    print(f"Conjunto de Interesses do Usuário (U): {userInterests}")
    print(f"Conjunto de Engajamento de Amigos (F): {friendEngagements}")
    print(f"Feed Resultante (Interseção U ∩ F): {feed}")
    
    # Proper Subset validation
    isProper = SetTheoryToolbox.isProperSubset(feed, allAvailablePosts)
    print(f"O feed personalizado é um subconjunto próprio de todas as postagens? {isProper}")
    
    # 3. Graph Generation
    graphPath = "01_conjunto_subconjuntos/feed_venn_diagram.png"
    print(f"\nGerando o gráfico do Diagrama de Venn em: '{graphPath}'...")
    simulation.generateVisualization(graphPath)
    print("Diagrama de Venn gerado com sucesso!")
