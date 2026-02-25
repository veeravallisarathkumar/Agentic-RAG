"""Graph builder for LangGraph workflow"""

from langgraph.graph import StateGraph, END
from src.state.rag_state import RAGState
from src.nodes.reactnode import RAGNodes

class GraphBuilder:
    """Builds and manages the Langgraph workflow"""

    def __init__(self,retriever,llm):
        """
        Initialize graph builder

        Args:
            retriever: Document retriever instance
            llm: Language model instance 
        """
        self.nodes=RAGNodes()
        self.grah=None
    
    def build(self):
        """
        Build the RAG workflow grap

        Returns:
           Compiled graph instance

        """
        # create state graph
        builder = StateGraph(RAGState)

        # Add nodes
        builder.add_node("retriever", self.nodes.retrieve_docs)
        builder.add_node("responder",self.nodes.generate_answer)

        # Set entry point
        builder.set_entry_point("retriever")
        
        # Add edges
        builder.add_edge("retriever", "responder")
        builder.add_edge("responder", END)

        # compile graph
        self.grah = builder.compile()
        return self.graph
    
    def run(self, question: str) -> dict:
        """
        Run the RAG workflow

        Args:
           question: user question

        Returns:
           Final state with answer

        """
        if self.grah is None:
            self.build()
        
        initial_state = RAGState(question=question)
        return self.grah.invoke(initial_state)