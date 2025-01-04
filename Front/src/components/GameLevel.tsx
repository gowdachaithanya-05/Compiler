import React from 'react';
import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { useToast } from '@/hooks/use-toast';
import { Textarea } from '@/components/ui/textarea';

interface GameLevelProps {
  level: number;
  code: string;
  solution: string;
  hint: string;
  onComplete: () => void;
}

const GameLevel: React.FC<GameLevelProps> = ({ level, code, solution, hint, onComplete }) => {
  const [userCode, setUserCode] = React.useState(code);
  const [showHint, setShowHint] = React.useState(false);
  const { toast } = useToast();

  React.useEffect(() => {
    setUserCode(code);
    setShowHint(false);
  }, [code, level]);

  const handleCodeChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setUserCode(e.target.value);
  };

  const checkSolution = () => {
    if (userCode.trim() === solution.trim()) {
      toast({
        title: "Level Complete! 🎮",
        description: "Great job! You've fixed the syntax error!",
        className: "font-retro",
      });
      onComplete();
    } else {
      toast({
        title: "Try Again! 🔄",
        description: "That's not quite right. Keep trying!",
        variant: "destructive",
        className: "font-retro",
      });
    }
  };

  return (
    <Card className="p-4 sm:p-6 bg-retro-dark border-retro-primary border-2">
      <h2 className="text-lg sm:text-xl font-retro text-retro-primary mb-4">Level {level}</h2>
      <div className="mb-4 relative">
        <Textarea
          value={userCode}
          onChange={handleCodeChange}
          className="w-full min-h-[150px] sm:min-h-[200px] p-3 sm:p-4 bg-gray-900 text-retro-light 
                   font-mono text-sm sm:text-base rounded border-2 border-retro-secondary 
                   focus:border-retro-primary focus:outline-none focus:ring-1 
                   focus:ring-retro-primary resize-none scrollbar-thin 
                   scrollbar-thumb-retro-secondary scrollbar-track-gray-900"
          spellCheck="false"
          style={{
            fontFamily: 'Consolas, Monaco, "Andale Mono", monospace',
            lineHeight: '1.5',
            tabSize: '2',
          }}
        />
      </div>
      <div className="flex flex-col sm:flex-row justify-between items-center gap-3 sm:gap-4">
        <Button
          onClick={() => setShowHint(!showHint)}
          variant="outline"
          className="w-full sm:w-auto font-retro text-xs sm:text-sm border-retro-secondary 
                   hover:bg-retro-secondary/20 transition-colors duration-200"
        >
          {showHint ? "Hide Hint" : "Show Hint"}
        </Button>
        <Button
          onClick={checkSolution}
          className="w-full sm:w-auto font-retro text-xs sm:text-sm bg-retro-primary 
                   hover:bg-retro-secondary text-white transition-colors duration-200 
                   pixel-border"
        >
          Check Solution
        </Button>
      </div>
      {showHint && (
        <div className="mt-4 p-3 sm:p-4 bg-retro-secondary/20 rounded border border-retro-secondary 
                      animate-in slide-in-from-bottom duration-300">
          <p className="text-retro-light font-retro text-xs sm:text-sm">{hint}</p>
        </div>
      )}
    </Card>
  );
};

export default GameLevel;