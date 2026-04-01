import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	FileReadTool
)





@CrewBase
class ExcelBatchPoliticalSentimentAnalysisCrew:
    """ExcelBatchPoliticalSentimentAnalysis crew"""

    
    @agent
    def data_file_reader(self) -> Agent:
        
        return Agent(
            config=self.agents_config["data_file_reader"],
            
            
            tools=[				FileReadTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
    
    @agent
    def batch_sentiment_processor(self) -> Agent:
        
        return Agent(
            config=self.agents_config["batch_sentiment_processor"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
    
    @agent
    def excel_output_generator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["excel_output_generator"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
    

    
    @task
    def read_comments_from_file(self) -> Task:
        return Task(
            config=self.tasks_config["read_comments_from_file"],
            markdown=False,
            
            
        )
    
    @task
    def batch_process_sentiment_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["batch_process_sentiment_analysis"],
            markdown=False,
            
            
        )
    
    @task
    def generate_excel_ready_output(self) -> Task:
        return Task(
            config=self.tasks_config["generate_excel_ready_output"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the ExcelBatchPoliticalSentimentAnalysis crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


